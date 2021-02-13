function sendMail(contactForm) {
  emailjs.send("gmail","walkies_owner", {
    "owner_username": contactForm.owner_username.value,
    "from_email": contactForm.email.value,

  })
  .then(
        function(response){
            console.log("SUCCESS", response);
        },
        function(error){
            console.log("FAILED", error);
        });

  return false;
}