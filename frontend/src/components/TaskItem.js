import { useState } from 'react';

import TaskForm from './TaskForm';

function TaskItem({ task, onUpdate, onDelete }) {
  const [isEditing, setIsEditing] = useState(false);

  const handleUpdate = (payload) => {
    onUpdate(task.id, payload);
    setIsEditing(false);
  };

  const handleDelete = () => {
    if (window.confirm(`¿Borrar la tarea "${task.name}"?`)) {
      onDelete(task.id);
    }
  };

  if (isEditing) {
    return (
      <li className="TaskItem TaskItem-editing">
        <TaskForm
          initialValues={task}
          submitLabel="Guardar"
          onSubmit={handleUpdate}
          onCancel={() => setIsEditing(false)}
        />
      </li>
    );
  }

  return (
    <li className="TaskItem">
      <span className="TaskItem-name">{task.name}</span>
      {task.due_date && <span className="TaskItem-date">{task.due_date}</span>}
      <button onClick={() => setIsEditing(true)}>Editar</button>
      <button onClick={handleDelete}>Borrar</button>
    </li>
  );
}

export default TaskItem;
