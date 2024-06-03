import datetime
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtGui import QPainter, QColor, QPen, QFont, QFontDatabase
from PyQt5.QtCore import Qt

class Canvas(QWidget):
    def __init__(self, parent, small_pixel_font):
        super().__init__(parent)
        self.setMinimumSize(1792, 400)
        self.colors = [QColor(36, 41, 46), QColor(155, 233, 168), QColor(64, 196, 99), QColor(0, 109, 44)]  # GitHub dark mode colors
        
        # Load pixelated font
        font_id = QFontDatabase.addApplicationFont('assets/press_start_2p.ttf')
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        self.font = QFont(font_family, 12)
        self.small_font = small_pixel_font
        
        self.current_date = datetime.date.today()
        self.dates = self.generate_dates()
        self.grid = [[0 for _ in range(len(self.dates[0]))] for _ in range(7)]  # Initialize grid based on dates
        self.months = self.generate_months()
        self.days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def paintEvent(self, event):
        painter = QPainter(self)
        self.drawGrid(painter)
    
    def drawGrid(self, painter):
        pen = QPen(Qt.gray, 1, Qt.SolidLine)
        painter.setPen(pen)
        painter.setFont(self.small_font)  # Use smaller font for days

        # Calculate the horizontal starting point to center the grid
        grid_width = len(self.dates[0]) * 20
        start_x = (self.width() - grid_width) // 2

        # Draw days
        for i, day in enumerate(self.days):
            painter.drawText(start_x - 35, i * 20 + 40, day)
        
        painter.setFont(self.font)  # Use regular font for months

        # Draw months
        for month, x_pos in self.months.items():
            painter.drawText(start_x + x_pos * 20 + 40, 25, month)

        # Draw grid
        for x in range(len(self.dates[0])):
            for y in range(7):
                if self.dates[y][x]:
                    color = self.colors[self.grid[y][x]]
                    painter.setBrush(color)
                    painter.drawRoundedRect(start_x + x * 20 + 40, y * 20 + 25, 15, 15, 3, 3)

    def mousePressEvent(self, event):
        grid_width = len(self.dates[0]) * 20
        start_x = (self.width() - grid_width) // 2
        x = (event.pos().x() - start_x - 40) // 20
        y = (event.pos().y() - 25) // 20
        if 0 <= x < len(self.dates[0]) and 0 <= y < 7:
            if self.dates[y][x] and self.dates[y][x] < self.current_date:
                QMessageBox.warning(self, "Invalid Date", "You cannot commit to past dates.")
                return
            self.grid[y][x] = (self.grid[y][x] + 1) % 4  # Cycle through colors
            self.update()

    def clearCanvas(self):
        self.grid = [[0 for _ in range(len(self.dates[0]))] for _ in range(7)]
        self.update()

    def generate_dates(self):
        year = self.current_date.year
        start_date = datetime.date(year, 1, 1)
        
        start_day_of_week = (start_date.weekday() + 1) % 7  # Adjust so Monday = 0, Sunday = 6
        num_days = 366 if self.is_leap_year(year) else 365

        dates = [[None for _ in range((num_days + start_day_of_week + 6) // 7)] for _ in range(7)]
        
        current_date = start_date
        for day in range(num_days):
            week = (day + start_day_of_week) // 7
            weekday = (day + start_day_of_week) % 7
            dates[weekday][week] = current_date
            current_date += datetime.timedelta(days=1)
        
        return dates

    def generate_months(self):
        months = {}
        for x in range(len(self.dates[0])):
            for y in range(7):
                if self.dates[y][x]:
                    month = self.dates[y][x].strftime('%b')
                    if self.dates[y][x].day <= 7 and month not in months:
                        months[month] = x
        return months

    def is_leap_year(self, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
