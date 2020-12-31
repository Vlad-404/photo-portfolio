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

// Handling of errors in Stripe
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
    // Prevents form from submitting,...
    ev.preventDefault();
    // ...prevents multiple submitions and...
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    // ...triggers a loading screen animation
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    // Checks if the save form info is checked or not
    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    // Gets the csrf token
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    // Creates object to pass it into the new view which can't go into the payment intent
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    // Returns the url where this data is used
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function () {
    // This function calls Stripe to confirm payment and gives it the required details
        stripe.confirmCardPayment(clientSecret, {
            // For payment...
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address:{
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        state: $.trim(form.county.value),
                    }
                }
            },
            // ...for shipping
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    postal_code: $.trim(form.postcode.value),
                    state: $.trim(form.county.value),
                }
            },
        }).then(function(result) {
            // Displays an error if something is wrong...
            if (result.error) {
                // Targets the div for messages and displays the message in the div
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                // Gives the user option to fix the error
                $(errorDiv).html(html);
                // Triggers a loading screen animation and after it's finished, lets user to fix the error(s)
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
            // ...or, submits the form if the payment is successfull
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        // If there's an error with posting the data to the view, reloads the page without charging the user(see code above)
        location.reload();
    })
});


// document.addEventListener('DOMContentLoaded', function() {
//     alert("JavaScript is working");
// }, false);