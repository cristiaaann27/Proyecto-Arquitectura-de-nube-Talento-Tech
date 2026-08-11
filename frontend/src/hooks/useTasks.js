import { useCallback, useEffect, useState } from 'react';

import * as taskApi from '../services/taskApi';

export default function useTasks() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const refresh = useCallback(async () => {
    setLoading(true);
    try {
      const fetchedTasks = await taskApi.getTasks();
      setTasks(fetchedTasks);
      setError(null);
    } catch (err) {
      setError('No se pudieron cargar las tareas');
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    refresh();
  }, [refresh]);

  const createTask = useCallback(
    async (payload) => {
      await taskApi.createTask(payload);
      await refresh();
    },
    [refresh]
  );

  const updateTask = useCallback(
    async (id, payload) => {
      await taskApi.updateTask(id, payload);
      await refresh();
    },
    [refresh]
  );

  const deleteTask = useCallback(
    async (id) => {
      await taskApi.deleteTask(id);
      await refresh();
    },
    [refresh]
  );

  return { tasks, loading, error, createTask, updateTask, deleteTask, refresh };
}
