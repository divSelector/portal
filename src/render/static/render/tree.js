function getDepth(el) {
    let depth = 0;
    while (el && (el = el.parentElement)) {
      if (el.tagName === "DETAILS") depth++;
    }
    return depth;
  }
  
  function maxDepth() {
    let m = 0;
    document.querySelectorAll(".json-root details").forEach((d) => {
      m = Math.max(m, getDepth(d));
    });
    return m;
  }
  
  document.getElementById("btnExpand").addEventListener("click", () => {
    const all = [...document.querySelectorAll(".json-root details")];
  
    // find shallowest *closed* level
    let nextDepth = Infinity;
    all.forEach((d) => {
      if (!d.open) nextDepth = Math.min(nextDepth, getDepth(d));
    });
  
    // if nothing closed, stop
    if (nextDepth === Infinity) return;
  
    // open all at that depth
    all.forEach((d) => {
      if (getDepth(d) === nextDepth) d.open = true;
    });
  });
  
  document.getElementById("btnCollapse").addEventListener("click", () => {
    const all = [...document.querySelectorAll(".json-root details")];
  
    // find deepest currently open depth
    let maxOpen = -1;
    all.forEach((d) => {
      if (d.open) maxOpen = Math.max(maxOpen, getDepth(d));
    });
  
    if (maxOpen < 0) return;
  
    // close all at that level
    all.forEach((d) => {
      if (getDepth(d) === maxOpen) d.open = false;
    });
  });
  
  document.addEventListener("keydown", (e) => {
    if (
      (e.key === "Enter" || e.key === " ") &&
      document.activeElement &&
      document.activeElement.tagName === "SUMMARY"
    ) {
      e.preventDefault();
      const details = document.activeElement.parentElement;
      details.open = !details.open;
    }
  });
  