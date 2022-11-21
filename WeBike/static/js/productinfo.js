function openPopup(){
    var popup = document.getElementById("shop_section");
    popup.classList.add("open_shop_section");
}

function closePopup(){
    var popup = document.getElementById("shop_section");
    popup.classList.remove("open_shop_section");
}

function changePhoto(banner_img) {
    var banner_img = banner_img;
    var display_img = document.getElementById("display_img");
    display_img.src = banner_img.src;
    cleanHalo();
    banner_img.className += " active";
}

function cleanHalo() {
    const banner_imgs = document.getElementsByName("banner_img");
    for (let i = 0; i < banner_imgs.length; i++) {
        banner_imgs[i].className = banner_imgs[i].className.replace(" active", "");
    }
}

function popupPhoto() {
    document.getElementById('popup_photo').style.display='block';
    const display_img = document.getElementById("display_img");
    const popup_photo_img = document.getElementById("popup_photo_img");
    popup_photo_img.src = display_img.src;
}

function AddToCart() {

}

function pay(){

}