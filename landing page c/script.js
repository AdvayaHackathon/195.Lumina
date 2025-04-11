document.addEventListener("DOMContentLoaded", () => {
  console.log("Lumina animation loaded");

  const text1 = "Not";
  const text2 = "Everyone";
  const text3 = "has someone...";
  const text4 = "But now, you do.";
  const text5 = "Talk. Heal. Feel heard — with Lumina.❤️";
  const typingText = document.querySelector(".typing-text");
  const typingText2 = document.querySelector(".typing-text-2");
  const typingText3 = document.querySelector(".typing-text-3");
  const typingText4 = document.querySelector(".typing-text-4");
  const bottomBtn = document.querySelector(".bottom-btn");
  let index = 0;
  let index2 = 0;
  let index3 = 0;
  let index4 = 0;
  let index5 = 0;

  function typeWriter(text, element, speed = 100) {
    if (index < text.length) {
      element.textContent += text.charAt(index);
      index++;
      setTimeout(() => typeWriter(text, element, speed), speed);
    }
  }

  function typeWriter2(text, element, speed = 100) {
    if (index2 < text.length) {
      element.textContent += text.charAt(index2);
      index2++;
      setTimeout(() => typeWriter2(text, element, speed), speed);
    }
  }

  function typeWriter3(text, element, speed = 100) {
    if (index3 < text.length) {
      element.textContent += text.charAt(index3);
      index3++;
      setTimeout(() => typeWriter3(text, element, speed), speed);
    }
  }

  function typeWriter4(text, element, speed = 100) {
    if (index4 < text.length) {
      element.textContent += text.charAt(index4);
      index4++;
      setTimeout(() => typeWriter4(text, element, speed), speed);
    }
  }

  function typeWriter5(text, element, speed = 100) {
    if (index5 < text.length) {
      element.textContent += text.charAt(index5);
      index5++;
      setTimeout(() => typeWriter5(text, element, speed), speed);
    }
  }

  // Start first word "not" after the fade-in animation
  setTimeout(() => {
    typeWriter(text1, typingText, 100);
  }, 3700);

  // Start "everyone" after "not" completes
  setTimeout(() => {
    typingText.textContent += " ";
    typeWriter2(text2, typingText, 100);
  }, 3700 + text1.length * 100 + 500);

  // Start "has someone..." on the second line
  setTimeout(() => {
    typeWriter3(text3, typingText2, 100);
  }, 3700 + (text1.length + text2.length + 1) * 100 + 1000);

  // Start "But now, you do." on a new line
  setTimeout(() => {
    typeWriter4(text4, typingText3, 100);
  }, 3700 + (text1.length + text2.length + 1 + text3.length) * 100 + 1500);

  // Start the tagline after all previous text is complete
  setTimeout(() => {
    typeWriter5(text5, typingText4, 100);
  }, 3700 + (text1.length + text2.length + 1 + text3.length + text4.length) * 100 + 2000);

  // Show the bottom button after all typing is complete with a longer delay
  setTimeout(() => {
    bottomBtn.style.opacity = "1";
    bottomBtn.style.transform = "scale(1)";
  }, 3700 + (text1.length + text2.length + 1 + text3.length + text4.length + text5.length) * 100 + 3500);
});
