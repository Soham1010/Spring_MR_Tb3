# 📦 SpringSwarm-MRS: Collaborative Object Transport 🐢🐢🐢

**SpringSwarm-MRS** is a ROS 2 Humble and Gazebo Classic simulation environment designed for researching Multi-Robot System (MRS) collaborative transport. It features three TurtleBot3 Burgers tethered to a common cargo box via simulated spring-damper couplings.

---

## 🚀 Features

* **Leader-Follower Architecture**
  Manual human control for the *Leader* and autonomous assistance from *Followers*.

* **Elastic Couplings**
  Real-time spring-damper physics implemented via prismatic joints.

* **Force Feedback**
  Integrated Force/Torque (FT) sensors that stream real-time tension data to the control nodes.

* **Visual Debugging**
  Color-coded agents for easy tracking:
  🔴 Leader | 🟢 Follower 1 | 🟡 Follower 2

---
<img width="589" height="343" alt="image" src="https://github.com/user-attachments/assets/99684d24-28e9-49af-815b-72c071de3302" />

## 🛠️ Installation & Setup

### 1. Prerequisites

Ensure you are running **Ubuntu 22.04** with **ROS 2 Humble**. Install required packages:

```bash
sudo apt update
sudo apt install ros-humble-turtlebot3-description \
                 ros-humble-turtlebot3-gazebo \
                 ros-humble-teleop-twist-keyboard
```

---

### 2. Workspace Setup

```bash
mkdir -p ~/mrs_ws/src
cd ~/mrs_ws/src

# Clone this repository here

cd ~/mrs_ws
colcon build --packages-select mrs_transport
source install/setup.bash
```

---

### 3. Fixing Visual Meshes (Important! 🖼️)

Gazebo Classic may fail to locate ROS mesh paths. Fix it with:

```bash
mkdir -p ~/.gazebo/models
ln -s /opt/ros/humble/share/turtlebot3_description ~/.gazebo/models/turtlebot3_description
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:~/.gazebo/models
```

---

## 🎮 How to Run

### Terminal 1: Launch Gazebo 🌏

Starts the simulation and spawns the 3-robot system:

```bash
export TURTLEBOT3_MODEL=burger
source ~/mrs_ws/install/setup.bash
ros2 launch mrs_transport spawn_system.launch.py
```

---

### Terminal 2: Start the Swarm Brain 🧠

Runs the follower controller node:

```bash
source ~/mrs_ws/install/setup.bash
ros2 run mrs_transport follower_controller.py
```

---

### Terminal 3: Manual Control 🕹️

Control the **Leader robot**:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard \
  --ros-args --remap cmd_vel:=/tb3_leader/cmd_vel
```

---

## 🔬 Technical Details

### 🧩 Spring Physics

The tethers are modeled as prismatic joints using Gazebo’s `implicitSpringDamper` plugin.

[
F_s = k(x - x_0) + c\dot{x}
]

Where:

* (k = 150.0 , \text{N/m}) (stiffness)
* (c = 5.0 , \text{Ns/m}) (damping)

---

### 🤖 Control Law

Followers use proportional control based on spring tension:

[
v_{\text{follower}} = K_p \cdot F_x
]

Where:

* (K_p = 0.05)

This allows followers to actively reduce tension and *share the load* with the leader.

---

## 🤝 Contributors & Acknowledgments

* **Faculty Advisor:** Aditya Bhatt
* **Contributor** Soham Mehra
* **Research Context:** Developed for the ADAMS Lab (Autonomous Design and Materials Systems) for collaborative robotics research

---

## 📝 License

This project is open-source and available under the **MIT License**.
