//JS Functionalities for List View Page

//Function for toggling edit form in detail view page
function toggleEditForm(item_id) {
    const editForm = document.querySelector(`#edit-form-${item_id}`);
    editForm.classList.toggle("hidden");
}

function untoggleEditForm(item_id) {
    const editForm = document.querySelector(`#edit-form-${item_id}`);
    editForm.classList.toggle("hidden");
}

//When clicked on close the pop up will be closed

function closePopup() {
    const popup = document.getElementById("add-item-popup");
    popup.style.display = "none";
}

//Confirm Delete Pop Up when a user tries to Delete an item in list view page
function confirmDelete() {
    console.log("confirmDelete function called");
    return confirm("Are you sure you want to delete this item");
}

// This function is responsible for calling sort function with the response given by user.
function submitSortForm() {
    document.getElementById('sort-form').submit();
}


