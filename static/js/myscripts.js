function searchCourse() {
var input, filter, cursos, cardContenedor, a, i, txtValue;
input = document.getElementById("search");
filter = input.value.toUpperCase();
cursos = document.getElementById("courseInfo");
cardContenedor = document.getElementsByClassName("cardContenedor");
for (i = 0; i < cardContenedor.length; i++) {
    a = cardContenedor[i].getElementsByTagName("h5")[0];
    txtValue = a.textContent || a.innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
        cardContenedor[i].classList.remove("d-none");
    } else {
        cardContenedor[i].classList.add("d-none");
    }

}

}