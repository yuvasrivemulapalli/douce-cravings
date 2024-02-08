from django.contrib import messages
from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.text import get_valid_filename

from actions.models import Action
from .forms import CommentForm
from .models import List_Of_Items, Catlog, Home, Best_Sellers, Review, Comment
from django.contrib.auth.models import User


# Edit View for the Edit Item Button
def edit_view(request, item_id):
    if request.method == 'POST':
        editing_item = get_object_or_404(List_Of_Items, id=item_id)
        previous_name = editing_item.title
        editing_item.title = request.POST.get('new_name')
        editing_item.price = request.POST.get('new_price')
        editing_item.description = request.POST.get('description')
        editing_item.save()

        user = User.objects.get(username=request.session.get("username"))
        action = Action(
            user=user,
            verb="edited the item",
            target=editing_item
        )
        action.save()

        messages.add_message(request, messages.INFO, "You have Successfully Edited: %s" % previous_name)
    return redirect(reverse('doucecravingsnew_app:item_details', args=[item_id]))


# Delete View for the Delete Item Button
def delete_view(request, item_id):
    if request.method == "POST":
        # Check if the user has admin privileges
        if request.session.get('role') == 'Admin':
            # Delete the item with the given item_id
            item_delete = List_Of_Items.objects.get(id=item_id)


            user = User.objects.get(username=request.session.get("username"))
            action = Action(
                user=user,
                verb="deleted the item",
                target=item_delete
            )
            action.save()
            item_delete.delete()

            messages.add_message(request, messages.WARNING, "You have Successfully Deleted: %s" % item_delete.title)

    return redirect('doucecravingsnew_app:list_of_items')


# Add Item View which renders to add_item page
def add_item(request):
    return render(request,
                  "doucecravings/html_files/add_item.html")


# List of Items View for the List of Items Page

def list_of_items(request):
    items = List_Of_Items.objects.all().order_by('id')  # initially ordering by id
    return render(request,
                  "doucecravings/html_files/list.html",
                  {"items": items}
                  )


# Home View for index.html
def home(request):
    slides = Home.objects.all();
    best_sellers = Best_Sellers.objects.all()
    actions = Action.objects.all()
    return render(request,
                  "doucecravings/html_files/index.html",
                  {"slides": slides, "best_sellers": best_sellers, "actions": actions})


# Item Details View for Detail View of an Item page

def item_details(request, item_id):
    object1 = get_object_or_404(List_Of_Items, id=item_id)
    object1.toppings = object1.toppings.split(',')

    # Get comments related to the item
    comments = Comment.objects.filter(item=object1).order_by('-timestamp')

    if request.method == 'POST':
        comment_text = request.POST.get('comment_text')
        if comment_text:
            # Retrieve the user instance using the stored username
            username = request.session.get('username')
            user = get_object_or_404(User, username=username)

            Comment.objects.create(user=user, item=object1, comment_text=comment_text)

    return render(request, "doucecravings/html_files/item_details.html", {
        "item_details": object1,
        "comments": comments,
    })

def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.session['username'] == comment.user.username or request.session['role'] == 'Admin':
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('doucecravingsnew_app:item_details', item_id=comment.item.id)
        else:
            form = CommentForm(instance=comment)
        return render(request, 'doucecravings/html_files/edit_comment.html', {'form': form, 'comment': comment})
    else:
        return HttpResponseForbidden("You don't have permission to edit this comment.")

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.session['username'] == comment.user.username or request.session['role'] == 'Admin':
        item_id = comment.item.id
        comment.delete()
        return redirect('doucecravingsnew_app:item_details', item_id=item_id)
    else:
        return HttpResponseForbidden("You don't have permission to delete this comment.")

# Review view for the review.html
def review(request):
    prev_reviews = Review.objects.all()
    return render(request,
                  "doucecravings/html_files/review.html",
                  {"prev_reviews": prev_reviews})


# Main View for the main.html
def main(request):
    catlog_items = Catlog.objects.all()
    return render(request,
                  "doucecravings/html_files/main.html",
                  {"catlog_items": catlog_items}
                  )


# Login View for login_page.html
def login_page(request):
    return render(request,
                  "users/user/login_page.html"
                  )



# Add View when clicked on Add Item Button
def add_view(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.session.get("username"))

        new_item = List_Of_Items(
            title=request.POST.get('title'),
            price=request.POST.get('price'),
            description=request.POST.get('description'),
            image=request.FILES.get('image'),
            user=user,
        )

        given_file_name = request.FILES.get('image').name
        cleaned_file_name = get_valid_filename(given_file_name)
        new_item.image = f"{cleaned_file_name}"


        new_item.save()

        action = Action(
            user=user,
            verb="created the new item",
            target=new_item
        )
        action.save()

        messages.add_message(request, messages.SUCCESS, "You have Successfully Added: %s" % new_item.title)

        # Pass the new item to the list.html template
        item_id = new_item.id

        return redirect(reverse('doucecravingsnew_app:item_details', args=[item_id]))

    items = List_Of_Items.objects.all()
    return render(request, 'doucecravings/html_files/list.html', {'items': items})


# View for Sort Items
def sort_items(request):
    global sorted_objects
    sort_option = request.GET.get('sort_option')
    print(f"Received sort_option: {sort_option}")

    objects = List_Of_Items.objects.all()

    if sort_option == 'price-low-to-high':
        sorted_objects = objects.order_by('price')
    elif sort_option == 'price-high-to-low':
        sorted_objects = objects.order_by('-price')
    elif sort_option == 'best-seller':
        sorted_objects = objects
    elif sort_option == 'reviews':
        sorted_objects = objects

    return render(request, 'doucecravings/html_files/list.html', {'items': sorted_objects})


# View to submit review in Review Page
def submit_review(request):
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if is_ajax and request.method == 'POST':
        review_text = request.POST.get('review_text')
        review = Review.objects.create(text=review_text)

        # Return the serialized review text as a JSON response
        return JsonResponse({
            'text': review.text,
        })


# View to get reviews from DB to display on reviews.html page
def get_reviews(request):
    reviews = Review.objects.all().order_by('-timestamp')
    review_data = [{'text': review.text} for review in reviews]
    return JsonResponse(review_data, safe=False)
