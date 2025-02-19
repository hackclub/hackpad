document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    document.querySelector(this.getAttribute('href')).scrollIntoView({behavior: 'smooth', block: 'start'});
  });
});
document.getElementById('joinBtn').addEventListener('click', function() {
  alert("good you clicked commie now scroll down");
});
const slider = document.querySelector('.slider');
const prevBtn = document.querySelector('.prev');
const nextBtn = document.querySelector('.next');
const sliderDotsContainer = document.querySelector('.slider-dots');
let slideIndex = 0;
let autoSlideInterval;
const images = [
  "./img/image.png",
  "./img/wholething.png",
  "./img/image-1.png",
"./img/image (16).png",
  "./img/image-3.png",
  "./img/image-4.png",
  "./img/image (17).png",
  "./img/image (16).png"
];
function createSlides() {
  slider.innerHTML = '';
  images.forEach((imgSrc, index) => {
    let slide = document.createElement('div');
    slide.className = 'slide';
    slide.innerHTML = `<img src="${imgSrc}" alt="Keyboard view ${index + 1}" class="transition-transform duration-500 hover:scale-105"/>`;
    slider.appendChild(slide);
  });
}
function updateSlider() {
  slider.style.transform = `translateX(-${slideIndex * 100}%)`;
  updateDots();
}
function createDots() {
  sliderDotsContainer.innerHTML = '';
  images.forEach((_, index) => {
    let dot = document.createElement('div');
    dot.className = `dot ${index === slideIndex ? 'active' : ''}`;
    dot.addEventListener('click', () => {
      slideIndex = index;
      updateSlider();
    });
    sliderDotsContainer.appendChild(dot);
  });
}
function updateDots() {
  document.querySelectorAll('.dot').forEach((dot, index) => {
    dot.classList.toggle('active', index === slideIndex);
  });
}
function transitionSlide(direction) {
  let currentSlide = slider.children[slideIndex];
  currentSlide.style.transition = 'transform 0.5s ease-out';
  currentSlide.style.transform = `translateX(${direction * 100}%)`;
  setTimeout(() => {
    currentSlide.style.transition = '';
    currentSlide.style.transform = '';
  }, 500);
}
createSlides();
createDots();
updateSlider();
prevBtn.addEventListener('click', () => {
  if (slideIndex > 0) {
    transitionSlide(1);
    slideIndex--;
    updateSlider();
  }
});
nextBtn.addEventListener('click', () => {
  if (slideIndex < images.length - 1) {
    transitionSlide(-1);
    slideIndex++;
    updateSlider();
  }
});
document.addEventListener('keydown', (e) => {
  if (e.key === 'ArrowLeft') prevBtn.click();
  if (e.key === 'ArrowRight') nextBtn.click();
});
let touchStartX = 0;
let touchEndX = 0;
slider.addEventListener('touchstart', e => { touchStartX = e.changedTouches[0].screenX; });
slider.addEventListener('touchend', e => { touchEndX = e.changedTouches[0].screenX; let diff = touchStartX - touchEndX; if (Math.abs(diff) > 50) { if (diff > 0) nextBtn.click(); else prevBtn.click(); } });
function startAutoSlide() {
  autoSlideInterval = setInterval(() => {
    slideIndex = (slideIndex + 1) % images.length;
    updateSlider();
  }, 5000);
}
function stopAutoSlide() {
  clearInterval(autoSlideInterval);
}
slider.addEventListener('mouseenter', stopAutoSlide);
slider.addEventListener('mouseleave', startAutoSlide);
startAutoSlide();
