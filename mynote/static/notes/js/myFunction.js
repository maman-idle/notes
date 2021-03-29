document.querySelector('.confirmation').addEventListener('click', confirmation);

//confirmation
function confirmation(e){
    if(!confirm('Are you sure')) e.preventDefault();
}