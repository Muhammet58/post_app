function onayMesajiGoster(event) {
    if (!confirm("Gönderiyi silmek istediğinizden emin misiniz ?")) {
        event.preventDefault(); /* Form submit işlemini iptal eder. */
    }
}




function toggleLike(icon) {
    const dislikeIcon = icon.parentNode.querySelector(".dislike-icon");
    if (icon.classList.contains("active")) {
        icon.classList.remove("active");
        const likeCountElement = icon.parentNode.querySelector(".like-count");
        const likeCount = parseInt(likeCountElement.textContent);
        likeCountElement.textContent = likeCount - 1;
    } else {
        icon.classList.add("active");
        if (dislikeIcon.classList.contains("active")) {
            dislikeIcon.classList.remove("active");
            const dislikeCountElement = icon.parentNode.querySelector(".dislike-count");
            const dislikeCount = parseInt(dislikeCountElement.textContent);
            dislikeCountElement.textContent = dislikeCount - 1;
        }
        const likeCountElement = icon.parentNode.querySelector(".like-count");
        const likeCount = parseInt(likeCountElement.textContent);
        likeCountElement.textContent = likeCount + 1;
    }
}

function toggleDislike(icon) {
    const likeIcon = icon.parentNode.querySelector(".like-icon");
    if (icon.classList.contains("active")) {
        icon.classList.remove("active");
        const dislikeCountElement = icon.parentNode.querySelector(".dislike-count");
        const dislikeCount = parseInt(dislikeCountElement.textContent);
        dislikeCountElement.textContent = dislikeCount - 1;
    } else {
        icon.classList.add("active");
        if (likeIcon.classList.contains("active")) {
            likeIcon.classList.remove("active");
            const likeCountElement = icon.parentNode.querySelector(".like-count");
            const likeCount = parseInt(likeCountElement.textContent);
            likeCountElement.textContent = likeCount - 1;
        }
        const dislikeCountElement = icon.parentNode.querySelector(".dislike-count");
        const dislikeCount = parseInt(dislikeCountElement.textContent);
        dislikeCountElement.textContent = dislikeCount + 1;
    }
}

