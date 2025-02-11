const monthYear = document.getElementById("monthYear");
const daysContainer = document.getElementById("daysContainer");
const prevMonthBtn = document.getElementById("prevMonth");
const nextMonthBtn = document.getElementById("nextMonth");

let currentDate = new Date();
function renderCalendar(date) {
    daysContainer.innerHTML = "";
    let year = date.getFullYear();
    let month = date.getMonth();
    let firstDay = new Date(year, month, 1).getDate();
    let totalDays = new Date(year, month + 1, 0).getDate();

    monthYear.textContent = date.toLocaleDateString("default", { month: "long", year: "numeric" });

    for (let i = 0; i < firstDay; i++) {
        let emptyDiv = document.createElement("div");
        daysContainer.appendChild(emptyDiv);
    }

    for (let day = 1; day <= totalDays; day++) {
        let dayDiv = document.createElement("div");
        dayDiv.textContent = day;
        dayDiv.classList.add("day");
        if (
            day === new Date().getDate() &&
            month === new Date().getMonth() &&
            year === new Date().getFullYear()
        ) {
            dayDiv.classList.add("today");
        }
        daysContainer.appendChild(dayDiv);
    }
}
prevMonthBtn.addEventListener("click",()=>{
    currentDate.setMonth(currentDate.getMonth()-1);
    renderCalendar(currentDate);
});
nextMonthBtn.addEventListener("click",()=>{
    currentDate.setMonth(currentDate.getMonth()+1);
    renderCalendar(currentDate);
});
renderCalendar(currentDate);
