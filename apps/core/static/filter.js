const menuToggle = document.getElementById("menu-toggle");
const sidebar = document.getElementById("sidebar");
const sidebarOverlay = document.getElementById("sidebar-overlay");

function toggleSidebar() {
  sidebar.classList.toggle("-translate-x-full");
  sidebarOverlay.classList.toggle("hidden");
}

menuToggle.addEventListener("click", toggleSidebar);
sidebarOverlay.addEventListener("click", toggleSidebar);

document.addEventListener("DOMContentLoaded", () => {
  // Dados de exemplo. No Django, você pode passar isso como JSON a partir da sua view.
  const statsData = {
    total: {
      cursosAtivos: 8,
      alunosAtivos: 1150,
      extAtivos: 112,
      alunosTotal: 1253,
      extTotal: 128,
    },
    2024.2: {
      cursosAtivos: 3,
      alunosAtivos: 450,
      extAtivos: 45,
      alunosTotal: 480,
      extTotal: 50,
    },
    2025.1: {
      cursosAtivos: 5,
      alunosAtivos: 700,
      extAtivos: 67,
      alunosTotal: 773,
      extTotal: 78,
    },
    2025.2: {
      cursosAtivos: 0,
      alunosAtivos: 0,
      extAtivos: 0,
      alunosTotal: 0,
      extTotal: 0,
    },
  };

  const statElements = {
    cursosAtivos: document.getElementById("stat-cursos-ativos"),
    alunosAtivos: document.getElementById("stat-alunos-ativos"),
    extAtivos: document.getElementById("stat-ext-ativos"),
    alunosTotal: document.getElementById("stat-alunos-total"),
    extTotal: document.getElementById("stat-ext-total"),
  };

  const dropdownContainer = document.getElementById(
    "semester-dropdown-container"
  );
  const dropdownButton = document.getElementById("semester-dropdown-button");
  const dropdownMenu = document.getElementById("semester-dropdown-menu");
  const selectedSemesterText = document.getElementById(
    "selected-semester-text"
  );

  function updateStats(semester) {
    const data = statsData[semester];
    if (!data) return;
    Object.keys(statElements).forEach((key) => {
      if (statElements[key]) {
        statElements[key].textContent =
          data[
            key
              .replace("stat-", "")
              .replace(/([A-Z])/g, " $1")
              .toLowerCase()
              .replace(" ", "")
          ].toLocaleString("pt-BR");
      }
    });
  }

  if (dropdownContainer && dropdownButton && dropdownMenu) {
    // Toggle dropdown visibility
    dropdownButton.addEventListener("click", (event) => {
      event.stopPropagation();
      dropdownMenu.classList.toggle("hidden");
    });

    // Handle option selection
    dropdownMenu.addEventListener("click", (event) => {
      const selectedOption = event.target.closest(".semester-option");
      if (!selectedOption) return;

      event.preventDefault(); // Prevent default <a> tag behavior

      const semester = selectedOption.dataset.semester;
      const semesterText = selectedOption.textContent;

      // Update button text
      if (selectedSemesterText) selectedSemesterText.textContent = semesterText;

      // Hide dropdown
      dropdownMenu.classList.add("hidden");

      // Update stats
      updateStats(semester);
    });

    // Close dropdown if clicked outside
    window.addEventListener("click", (event) => {
      if (!dropdownContainer.contains(event.target)) {
        dropdownMenu.classList.add("hidden");
      }
    });
  }

  // Inicia com os dados totais
  updateStats("total");
});
