
const overlay = document.getElementById("overlay");
const overlayImg = document.getElementById("overlay-img");

document.querySelectorAll('.my-img').forEach(img => {
    img.onclick = function() {
        overlay.style.display = "flex";
        overlayImg.src = this.src;
    }
});

function closeImg() {
    overlay.style.display = "none";
    overlayImg.src = "";
}
