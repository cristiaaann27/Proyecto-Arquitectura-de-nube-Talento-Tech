import TaskItem from './TaskItem';

function TaskList({ tasks, loading, error, onUpdate, onDelete }) {
  if (loading) {
    return <p>Cargando tareas...</p>;
  }

  if (error) {
    return <p className="TaskList-error">{error}</p>;
  }

  if (tasks.length === 0) {
    return <p>No tienes tareas.</p>;
  }

  return (
    <ul className="TaskList">
      {tasks.map((task) => (
        <TaskItem key={task.id} task={task} onUpdate={onUpdate} onDelete={onDelete} />
      ))}
    </ul>
  );
}

export default TaskList;
