const exampleModal = document.getElementById("exampleModal");
let videoid;

// modal 창 열기
exampleModal.addEventListener("show.bs.modal", function (event) {
  const button = event.relatedTarget;

  const title = button.getAttribute("data-bs-title");
  const desc = button.getAttribute("data-bs-desc");
  const videoID = button.getAttribute("data-bs-videoID");
  const modalTitle = exampleModal.querySelector(".modal-title");
  const modalDesc = exampleModal.querySelector(".modal-desc");
  const modalVideo = exampleModal.querySelector(".modal-video");
  videoid = videoID;

  modalVideo.src = `https://www.youtube.com/embed/${videoID}?autoplay=1&mute=1&loop=1&playlist=${videoID}`;
  modalTitle.textContent = title;
  modalDesc.textContent = desc;
  getLike();
  getComment();
});

exampleModal.addEventListener("hidden.bs.modal", function () {
  const modalVideo = exampleModal.querySelector(".modal-video");
  modalVideo.src = "";
});
