//Problem: Hints are shown even when form is valid
//Solution: Hide and show them at appropriate times
var $email = $("#email");
var $password = $("#password");

//Hide hints
$("form span").hide();


function isEmailValid() {
  var validationEmail = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  if($email.val().match(validationEmail)){
    return true;
  }
  else{
    return false;
  }
}

function isPasswordValid() {
  if($password.val().length > 8)
  {
    return true;
  }
  else
  {
    return false;
  }
}


function canSubmit() {
  if(isPasswordValid() == true 
  && isEmailValid() == true )
  {
    return true;
  }
  else
  {
    return false;
  }
}


function emailEvent(){
  //Find out if email is valid 
  if(isEmailValid()) {
    //Hide hint if valid
    $email.next().hide();
  } else {
    //else show hint
    $email.next().show();
  }
} 

function passwordEvent(){
    //Find out if password is valid  
    if(isPasswordValid()) {
      //Hide hint if valid
      $password.next().hide();
    } else {
      //else show hint
      $password.next().show();
    }
}


function enableSubmitEvent() {
  $("#submit").prop("disabled", !canSubmit()); 
}

//When event happens on email input
$email.focus(emailEvent).keyup(emailEvent).keyup(enableSubmitEvent);

//When event happens on password input
$password.focus(passwordEvent).keyup(passwordEvent).keyup(enableSubmitEvent);


enableSubmitEvent();