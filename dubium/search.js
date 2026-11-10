"use strict";

// EN: Search is a local enhancement. The full catalogue is present in the HTML.
// LA: Quaestio localis indicem adiuvat. Index integer in HTML iam adest.
const panel = document.querySelector("[data-search-panel]");
const input = panel.querySelector("input");
const status = panel.querySelector("[data-count]");
const groups = [...document.querySelectorAll("[data-group]")];
const languageLinks = [...document.querySelectorAll("[data-language]")];

function normalise(text) {
  return text.normalize("NFD").replace(/\p{Diacritic}/gu, "").toLowerCase();
}

const entries = groups.map(group => ({
  group,
  cards: [...group.querySelectorAll("[data-entry]")].map(card => ({
    card,
    text: normalise(card.textContent.replace(/\s+/g, " ")),
  })),
}));

function filter() {
  const words = normalise(input.value).trim().split(/\s+/).filter(Boolean);
  let visible = 0;
  for (const {group, cards} of entries) {
    let matches = 0;
    for (const {card, text} of cards) {
      const match = words.every(word => text.includes(word));
      card.hidden = !match;
      if (match) matches++;
    }
    group.hidden = matches === 0;
    visible += matches;
  }
  status.textContent = visible ? `${status.dataset.label} · ${visible}` : status.dataset.empty;
}

// EN: Follow a permalink even if the search hid it. Keep it when changing language.
// LA: Nexum stabilem sequere, etiamsi filtrum eum celavit. Eum mutata lingua serva.
function revealFragment() {
  let target;
  try {
    target = document.getElementById(decodeURIComponent(location.hash.slice(1)));
  } catch {
    return;
  }
  for (const link of languageLinks) {
    const url = new URL(link.getAttribute("href"), location.href);
    url.hash = target ? target.id : "";
    link.href = url.href;
  }
  if (!target) return;
  if (target.closest("[hidden]")) {
    input.value = "";
    filter();
  }
  const details = target.closest("details");
  if (details) details.open = true;
  target.scrollIntoView();
}

input.addEventListener("input", filter);
window.addEventListener("hashchange", revealFragment);
panel.hidden = false;
filter();
revealFragment();
