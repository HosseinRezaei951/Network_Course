//Problem: Hints are shown even when form is valid
//Solution: Hide and show them at appropriate times
var $email = $("#email");
var $subject = $("#subject");

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

function isSubjectValid() {
    return $subject.val().length > 0;
}
  

function canSubmit() {
  if(isEmailValid() == true &&
  isSubjectValid() == true)
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

function subjectEvent(){
    //Find out if subject is valid 
    if(isSubjectValid()) {
      //Hide hint if valid
      $subject.next().hide();
    } else {
      //else show hint
      $subject.next().show();
    }
  } 



function enableSubmitEvent() {
  $("#submit").prop("disabled", !canSubmit()); 
}

//When event happens on email input
$email.focus(emailEvent).keyup(emailEvent).keyup(enableSubmitEvent);

//When event happens on subject input
$subject.focus(subjectEvent).keyup(subjectEvent).keyup(enableSubmitEvent);

enableSubmitEvent();