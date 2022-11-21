/*
    Function to load more
*/
function loadMore() {
    let loadMoreBtn = document.querySelector('#load-more');
    let currentItem = 6;
    
    loadMoreBtn.onclick = () =>{
        let boxes = [...document.querySelectorAll('.container .box-container .box')];
        for (var i = currentItem; i < currentItem + 6; i++){
            try{
                boxes[i].style.display = 'inline-block';
            }
            catch(err){
                continue;
            }
        }
        currentItem += 6;
    
        if(currentItem >= boxes.length){
            loadMoreBtn.style.display = 'none';
        }
    }
}

/*
    Function to open suggestions box
*/
function openForm() {
    document.getElementById("suggestions-form").style.display = "block";
}

/*
    Function to close suggestions box
*/
function closeForm() {
    document.getElementById("suggestions-form").style.display = "none";
}

/*
    Function to load a self written article
*/
function loadArticle(image, title, preview) {
    document.getElementById("admin-blog").style.display = "block";
    document.getElementById("container").setAttribute("id", "body-blur");

    document.getElementById("admin-image").src = image;
    document.getElementById("admin-heading").innerHTML = title;
    console.log(preview.childNodes[3].innerHTML);
    document.getElementById("pre-format").innerHTML = preview.childNodes[3].innerHTML;
    // document.getElementById("pre-format").innerHTML = document.getElementById("innerText")
    // .innerHTML;

}


function closeArticle() {
    document.getElementById("admin-blog").style.display = "none";
    document.getElementById("body-blur").setAttribute("id", "container");
}

function openEditDialog() {
    var popup = document.getElementById("edit_blog_section");
    popup.classList.add("open_edit_blog_section");
}

function closeEditDialog() {
    var popup = document.getElementById("edit_blog_section");
    popup.classList.remove("open_edit_blog_section");
}