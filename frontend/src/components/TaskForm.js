import { useState } from 'react';

function TaskForm({ initialValues, submitLabel = 'Agregar tarea', onSubmit, onCancel }) {
  const [name, setName] = useState(initialValues?.name || '');
  const [dueDate, setDueDate] = useState(initialValues?.due_date || '');

  const handleSubmit = (event) => {
    event.preventDefault();
    if (!name.trim()) {
      return;
    }
    onSubmit({ name: name.trim(), due_date: dueDate || null });
    if (!initialValues) {
      setName('');
      setDueDate('');
    }
  };

  return (
    <form className="TaskForm" onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Nombre de la tarea"
        value={name}
        onChange={(event) => setName(event.target.value)}
      />
      <input
        type="date"
        value={dueDate || ''}
        onChange={(event) => setDueDate(event.target.value)}
      />
      <button type="submit" disabled={!name.trim()}>
        {submitLabel}
      </button>
      {onCancel && (
        <button type="button" onClick={onCancel}>
          Cancelar
        </button>
      )}
    </form>
  );
}

export default TaskForm;
