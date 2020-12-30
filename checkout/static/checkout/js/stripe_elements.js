/* 
    Javascript from https://stripe.com/docs/payments/accept-a-payment 
    and css from https://stripe.com/docs/stripe-js
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Montserrat", "Open Sans", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handling of errors with Stripe
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Form submit handling
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    // Prevents deafult card behaviour
    ev.preventDefault();
    // Prevents multiple submitions
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    // Triggers a loading screen animation
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
    // This function calls Stripe to confirm payment and gives it the required details
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        // Displays an error if something is wrong...
        if (result.error) {
            // Targets the div for messages and provides content
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            // Gives the user option to fix the error
            $(errorDiv).html(html);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
            // Triggers a loading screen animation
            $('#payment-form').fadeToggle(100);
            $('#loading-overlay').fadeToggle(100);
        } else {
        // ...or, submits if the payment is successfull
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});


// document.addEventListener('DOMContentLoaded', function() {
//     alert("JavaScript is working");
// }, false);