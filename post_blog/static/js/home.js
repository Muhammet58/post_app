function onayMesajiGoster(event) {
    if (!confirm("Gönderiyi silmek istediğinizden emin misiniz ?")) {
        event.preventDefault(); /* Form submit işlemini iptal eder. */
    }
}



let likeCount = 0;
let dislikeCount = 0;

function like() {
    const likeIcon = document.getElementById('likeIcon');
    const dislikeIcon = document.getElementById('dislikeIcon');
    const likeCountSpan = document.getElementById('likeCount');
    const dislikeCountSpan = document.getElementById('dislikeCount');

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

