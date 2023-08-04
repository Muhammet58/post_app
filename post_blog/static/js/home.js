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









/*
let likeCount = 0;
let dislikeCount = 0;

function like() {
    /*$('[name^="likebtn-"]').click(fuction(){if kısmını buraya girersin})*/
/* $("i[name^='likebtn']").ready('click', function(){
})*/
/*$('.card-footer').parentElement.parentElement.getElementsByClassName('card')*/
/*    post_ids = document.getElementsByName('likebtn');
    post_ids.forEach((post_id, index)=>{
        var pk = post_id['id'].split('-')[1];
        const likeIcon = document.getElementById('likeIcon-' + pk);
        const dislikeIcon = document.getElementById('dislikeIcon-' + pk);
        const likeCountSpan = document.getElementById('likeCount-' + pk);
        const dislikeCountSpan = document.getElementById('dislikeCount-' + pk);
        
        if (!likeIcon.classList.contains('liked')) {
            likeIcon.classList.add('liked');
            likeCount++;
            likeCountSpan.textContent = likeCount;
        } else {
            likeIcon.classList.remove('liked');
            likeCount--;
            likeCountSpan.textContent = likeCount;
        }
        
        if (dislikeIcon.classList.contains('disliked')) {
            dislikeIcon.classList.remove('disliked');
            dislikeCount--;
            dislikeCountSpan.textContent = dislikeCount;
        }
    })


}

function dislike() {
    const likeIcon = document.getElementById('likeIcon');
    const dislikeIcon = document.getElementById('dislikeIcon');
    const likeCountSpan = document.getElementById('likeCount');
    const dislikeCountSpan = document.getElementById('dislikeCount');

    if (!dislikeIcon.classList.contains('disliked')) {
        dislikeIcon.classList.add('disliked');
        dislikeCount++;
        dislikeCountSpan.textContent = dislikeCount;
    } else {
        dislikeIcon.classList.remove('disliked');
        dislikeCount--;
        dislikeCountSpan.textContent = dislikeCount;
    }

    if (likeIcon.classList.contains('liked')) {
        likeIcon.classList.remove('liked');
        likeCount--;
        likeCountSpan.textContent = likeCount;
    }
}
*/