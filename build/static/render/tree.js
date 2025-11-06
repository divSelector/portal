function isFolder(element) {
  return element.tagName === 'DETAILS' &&
         element.querySelector('summary > .key') &&
         element.querySelector('.node');
}

function getAllFolders() {
  return Array.from(document.querySelectorAll('details')).filter(isFolder);
}

function getParentFolder(folder) {
  let parent = folder.parentElement;
  while (parent) {
    if (isFolder(parent)) {
      return parent;
    }
    parent = parent.parentElement;
  }
  return null;
}

function getDirectChildFolders(folder) {
  const node = folder.querySelector('.node');
  if (!node) return [];
  return Array.from(node.children).filter(child => isFolder(child));
}

function getFullPath(folder) {
  const key = folder.querySelector('summary > .key')?.textContent;
  if (!key) return null;
 
  const parent = getParentFolder(folder);
  const parentPath = parent ? getFullPath(parent) : '';
  return parentPath ? `${parentPath}>${key}` : key;
}

function loadPersistedStates() {
  getAllFolders().forEach(folder => {
    const children = getDirectChildFolders(folder);
    if (children.length > 0) return;
    const path = getFullPath(folder);
    if (path && localStorage.getItem(path) === 'true') {
      const key = folder.querySelector('summary > .key')?.textContent;
      folder.classList.add('was-opened');
    }
  });
}

function evaluateFolder(folder, isLoad = false) {
  const key = folder.querySelector('summary > .key')?.textContent;

  if (!isLoad && !folder.open) {
    return;
  }
  const children = getDirectChildFolders(folder);

  if (children.length === 0) {
    if (!isLoad && !folder.classList.contains('was-opened')) {
      folder.classList.add('was-opened');

      const path = getFullPath(folder);
      if (path) {
        localStorage.setItem(path, 'true');
      }
    }
    return;
  }

  const allChildrenAchieved = children.every(c => c.classList.contains('was-opened'));
  if (allChildrenAchieved) {
    if (!folder.classList.contains('was-opened')) {
      folder.classList.add('was-opened');
    }
  } else {
    console.log('Not all children achieved, skipping mark for:', key);
  }
}

function initEval(folder, isLoad = false) {
  getDirectChildFolders(folder).forEach(child => initEval(child, isLoad));
  evaluateFolder(folder, isLoad);
}

function updateFromThisFolder(folder) {
  evaluateFolder(folder, false);
  let parent = getParentFolder(folder);
  while (parent) {
    evaluateFolder(parent, false);
    parent = getParentFolder(parent);
  }
}

function scrollOpenedContentIntoView(folder) {
  folder.scrollIntoView({
    behavior: 'smooth',
    block: 'start'
  });
}

let isBulkToggle = false;

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

  let nextDepth = Infinity;
  all.forEach((d) => {
    if (!d.open) nextDepth = Math.min(nextDepth, getDepth(d));
  });

  if (nextDepth === Infinity) return;

  isBulkToggle = true;
  all.forEach((d) => {
    if (getDepth(d) === nextDepth) d.open = true;
  });
  setTimeout(() => { isBulkToggle = false; }, 100);
});

document.getElementById("btnCollapse").addEventListener("click", () => {
  const all = [...document.querySelectorAll(".json-root details")];

  let maxOpen = -1;
  all.forEach((d) => {
    if (d.open) maxOpen = Math.max(maxOpen, getDepth(d));
  });

  if (maxOpen < 0) return;

  isBulkToggle = true;
  all.forEach((d) => {
    if (getDepth(d) === maxOpen) d.open = false;
  });
  setTimeout(() => { isBulkToggle = false; }, 100);
});


document.getElementById("btnMarkUnseen").addEventListener("click", () => {
  localStorage.clear();
  getAllFolders().forEach(folder => {
    folder.classList.remove('was-opened');
  });
  document.querySelectorAll(".json-root details[open]").forEach(d => {
    d.open = false;
  });
});

getAllFolders().forEach(folder => {
  folder.addEventListener('toggle', () => {
    const key = folder.querySelector('summary > .key')?.textContent;
    setTimeout(() => {
      updateFromThisFolder(folder);
      if (folder.open && !isBulkToggle) {
        scrollOpenedContentIntoView(folder);
      }
    }, 0);
  });
});

loadPersistedStates();

const roots = getAllFolders().filter(f => !getParentFolder(f));
roots.forEach(root => initEval(root, true));