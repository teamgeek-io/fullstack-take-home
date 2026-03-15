import { useEffect, useState } from "react";
import { getTasks } from "./api/client";

export default function App() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    getTasks().then(setTasks);
  }, []);

  return (
    <div>
      <h1>Tasks</h1>

      {tasks.map((task) => (
        <div key={task.id}>
          {task.title} — {task.status}
        </div>
      ))}
    </div>
  );
}
