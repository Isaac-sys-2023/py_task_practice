const API_URL = 'http://localhost:5220/api/tareas';

const taskList = document.getElementById('task-list');
const taskForm = document.getElementById('task-form');
const taskTitleInput = document.getElementById('task-title');
const taskContextInput = document.getElementById('task-context');
const taskAuthorInput = document.getElementById('task-author');

const taskEditTitleInput = document.getElementById('task-title-edit');
const taskEditContextInput = document.getElementById('task-context-edit');
const taskEditAuthorInput = document.getElementById('task-author-edit');

async function fetchTasks() {
  const res = await fetch(API_URL);
  const tasks = await res.json();
  console.log(tasks);


  taskList.innerHTML = '';
  tasks.forEach(task => {
    const li = document.createElement('li');
    li.className = 'flex justify-between items-center bg-gray-100 px-4 py-2 rounded';

    li.innerHTML = `
      <span>${task.titulo}</span>

      <div class="flex justify-center gap-2">
        <button onclick='openModal(${JSON.stringify(task)})' class="bg-yellow-400 px-4 py-2 rounded text-white hover:bg-yellow-500">Editar</button>
        <button onclick="deleteTask(${task.id})" class="bg-red-600 px-4 py-2 rounded text-white hover:bg-red-700">Eliminar</button>
      </div>
      `;
    taskList.appendChild(li);
  });
}

let currentEditId = null;

function openModal(task) {
  currentEditId = task.id;
  taskEditTitleInput.value = task.titulo;
  taskEditContextInput.value = task.contexto;
  taskEditAuthorInput.value = task.autor;
  document.getElementById('modal-edit').showModal();
}

function closeModal() {
  document.getElementById('modal-edit').close();
}

async function addTask(title, context, author) {
  await fetch(API_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      titulo: title,
      contexto: context,
      autor: author
    })
  });
  fetchTasks();
}

async function deleteTask(id) {
  await fetch(`${API_URL}/${id}`, {
    method: 'DELETE'
  });
  fetchTasks();
}

async function updateTask(id, title, context, author) {
  await fetch(`${API_URL}/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      titulo: title,
      contexto: context,
      autor: author
    })
  })
  taskEditTitleInput.value = '';
  taskEditContextInput.value = '';
  taskEditAuthorInput.value = '';
  fetchTasks();
}

document.getElementById('edit-form').addEventListener('submit', e => {
  e.preventDefault();
  const title = taskEditTitleInput.value.trim();
  const context = taskEditContextInput.value.trim();
  const author = taskEditAuthorInput.value.trim();

  if (title) {
    updateTask(currentEditId, title, context, author);
    closeModal();
  }
});



taskForm.addEventListener('submit', e => {
  e.preventDefault();
  const title = taskTitleInput.value.trim();
  const context = taskContextInput.value.trim();
  const author = taskAuthorInput.value.trim();
  if (title) {
    addTask(title, context, author);
    taskTitleInput.value = '';
    taskContextInput.value = '';
    taskAuthorInput.value = '';
  }
});

fetchTasks();
