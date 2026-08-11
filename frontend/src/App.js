import './App.css';
import TaskForm from './components/TaskForm';
import TaskList from './components/TaskList';
import VoiceCommand from './components/VoiceCommand';
import useTasks from './hooks/useTasks';

function App() {
  const { tasks, loading, error, createTask, updateTask, deleteTask, refresh } = useTasks();

  return (
    <div className="App">
      <h1>Voice Command Task Assistant</h1>

      <VoiceCommand onCommandSuccess={refresh} />

      <TaskForm onSubmit={createTask} />
      <TaskList
        tasks={tasks}
        loading={loading}
        error={error}
        onUpdate={updateTask}
        onDelete={deleteTask}
      />
    </div>
  );
}

export default App;
