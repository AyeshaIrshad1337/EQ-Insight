const signUpButton=document.getElementById('signUpButton');
const signInButton=document.getElementById('signInButton');
const signInForm=document.getElementById('signIn');
const signUpForm=document.getElementById('signup');

signUpButton.addEventListener('click',function(){
    signInForm.style.display="none";
    signUpForm.style.display="block";
})
signInButton.addEventListener('click', function(){
    signInForm.style.display="block";
    signUpForm.style.display="none";
})
var cb = document.querySelector('#cb-toggle');
var toggleStateInput = document.querySelector('#toggleState');
cb.addEventListener('click', function() {
    var currentState;
    if (cb.checked) {
        currentState = 'HR';
    } else {
        currentState = 'User';
    }
    toggleState.value = currentState; // Update the hidden input field
    console.log("Toggle state updated:", currentState);
    var stateSpan = document.querySelector('#toggle-state');
    stateSpan.innerHTML = currentState;
}, false);



// For sign-up form toggle button
var cbSignup = document.querySelector('#cb-toggle-signup');
var toggleStateSignup = document.querySelector('#toggleStateSignup');
var companyNameGroup = document.getElementById('companyNameGroup');

cbSignup.addEventListener('click', function() {
    var currentState;
    if (cbSignup.checked) {
        currentState = 'HR';
        companyNameGroup.style.display = 'block'; // Show company name field
    } else {
        currentState = 'User';
        companyNameGroup.style.display = 'none'; // Hide company name field
    }
    toggleStateSignup.value = currentState; // Update the hidden input field
    var stateSpan = document.querySelector('#toggle-state-signup');
    stateSpan.innerHTML = currentState;
}, false);
