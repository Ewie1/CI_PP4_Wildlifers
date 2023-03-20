

const deleteEnrollment = document.getElementById("btn-delete")



deleteEnrollment.addEventListener("click", confirmation)

function confirmation() {
  let modal = document.getElementById("delete");
  modal.classList.add("show-modal");
  console.log('hello')
}

confirmation()

/*setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
  }, 1500);

setTimeout()*/

$(document).ready(function () {
  setTimeout(function () {
      let messages = document.getElementById("msg");
      let alert = new bootstrap.Alert(messages);
      alert.close();
  }, 3000);
});