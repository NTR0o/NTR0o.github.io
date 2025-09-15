const activeFilters = [];

const groups = {
  genre: ["hip-hop", "rnb", "pop", "cinematic"],
  type: ["mixes", "remix"],
  role: ["production", "feature"]
};

function filterSelection(category) {
  const galleryItems = document.querySelectorAll(".song");

  // Reset filters when "All" is clicked
  if (category.toLowerCase() === "all") {
    activeFilters.length = 0; 
  } else {
    const idx = activeFilters.indexOf(category);
    if (idx > -1) {
      activeFilters.splice(idx, 1); // remove if clicked again
    } else {
      activeFilters.push(category); // add filter
    }
  }

  // Update gallery visibility
  galleryItems.forEach(item => {
    const categories = item.dataset.category.toLowerCase().split(" ");
    const shouldShow = activeFilters.length === 0 || matchesGroups(categories, activeFilters);
    item.style.display = shouldShow ? "block" : "none";
  });

  // Update filter tags (don’t include "All")
  updateActiveFiltersUI();
}

function matchesGroups(categories, filters) {
  return Object.values(groups).every(group => {
    const selectedInGroup = filters.filter(f =>
      group.includes(f.toLowerCase())
    );
    return (
      selectedInGroup.length === 0 || 
      selectedInGroup.some(f => categories.includes(f.toLowerCase()))
    );
  });
}

function updateActiveFiltersUI() {
  const container = document.querySelector(".activeFilters");
  container.innerHTML = "";

  activeFilters.forEach(f => {
    const tag = document.createElement("span");
    tag.textContent = f;
    tag.classList.add("filterTag");

    const x = document.createElement("button");
    x.textContent = "x";
    x.classList.add("removeFilter");
    x.onclick = () => filterSelection(f);

    tag.appendChild(x);
    container.appendChild(tag);
  });
}
