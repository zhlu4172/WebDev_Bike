const visibilityBtn = document.getElementById("visibilityBtn");
visibilityBtn.addEventListener("click", toggle)
function toggle() {
    const passwordInput = document.getElementById("password")
    const password2Input = document.getElementById("password2")
    const icon = document.getElementById("icon")
    if(passwordInput.type === "password") {
        passwordInput.type = "text"
        password2Input.type = "text"
        icon.innerText = "visibility_off"
    } else {
        passwordInput.type = "password"
        password2Input.type = "password"
        icon.innerText = "visibility"
    }
}