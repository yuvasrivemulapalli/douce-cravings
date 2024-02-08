// Using event delegation to handle clicks on the "Add to Cart" button
console.log("submit is being accessed");
$(document).on('click', '.cart-button', function () {
    const $button = $(this);
    const $successMessage = $button.siblings('.added-success');
    $button.html('<i class="fas fa-check"></i> Item Added');
    $successMessage.fadeIn();
    setTimeout(function () {
        $successMessage.fadeOut();
    }, 3000);
});


