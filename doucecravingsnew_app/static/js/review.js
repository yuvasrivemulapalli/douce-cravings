// JS functionalities for Review Page(Adding reviews) using AJAX

// Functionality for appending the review entered by user to the reviews list
$(document).ready(function () {
    function loadReviews() {
        $.ajax({
            url: "/get_reviews/",
            type: "GET",
            dataType: "json",
            success: function (data) {
                $('#reviews-list').empty();
                data.forEach(function (review) {
                    var listItem = $('<li>').text(review.text);
                    $('#reviews-list').prepend(listItem);
                });
            },
            error: function (xhr, status, errorThrown) {
                console.log('Error loading reviews: ' + errorThrown);
            }
        });
    }

    //function to toggle the reviews when clicked on the ALL REVIEWS button
    $('#toggle-reviews-button').click(function () {
        $('#reviews-box').slideToggle();
        if ($('#reviews-box').is(':visible')) {
            loadReviews();
        }
    });

    // When clicked on submit button the review will be stored in the db and will be displayed in the review-container along with the previous reviews.
    $('#submit-button-review').click(function () {
        const reviewText = $('#user-review').val();
        $.ajax({
            url: $('#submit-button-review').data('ajax_url'),
            type: 'POST',
            data: {
                review_text: reviewText,
                csrfmiddlewaretoken: csrftoken,
            },
            dataType: 'json',
            success: function (data) {
                $('#user-review').val('');
                $('#reviews-box').slideToggle();
                loadReviews();
            },
            error: function (xhr, status, errorThrown) {
                alert('Sorry, there was a problem!');
                console.log('Error: ' + errorThrown);
            },
        });
    });
    $('#reviews-box').hide();
});

//csrf function
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');