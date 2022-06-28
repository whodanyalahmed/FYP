var getValue = document.getElementById("values");
var but = document.getElementById("searchBut");

but.addEventListener("click", () => {
    if (getValue.value == "") {
        alert("Please enter phone name!");
        return;
    } else {
        sessionStorage.setItem("user", JSON.stringify(getValue.value.toLowerCase()));
        getValue.value = "";
        changePage();
    }

});

function changePage() {
    window.location.href = "Results/results.html";
}