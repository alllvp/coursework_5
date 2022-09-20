from dataclasses import dataclass

from skills import Skill, FuryPunch, HardShot


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


"""
Имя: "Воин"
Очки здоровья: 60.0
Очки выносливости: 30.0
Модификатор атаки: 0.8
Модификатор выносливости: 0.9
Модификатор брони: 1.2
Умение: Свирепый пинок
"""

# Инициализируем экземпляр класса UnitClass и присваиваем ему необходимые значения аттрибуотов
WarriorClass = UnitClass(
    name='Воин',
    max_health=60,
    max_stamina=30,
    attack=0.8,
    stamina=0.9,
    armor=1.2,
    skill=FuryPunch(),
)

"""
Имя: "Вор"
Очки здоровья: 50.0
Очки выносливости: 25.0
Модификатор атаки: 1.5
Модификатор выносливости: 1.2
Модификатор брони: 1.0
Умение: Мощный укол
"""
# действуем так же как и с войном
ThiefClass = UnitClass(
    name='Вор',
    max_health=50,
    max_stamina=25,
    attack=1.5,
    stamina=1.2,
    armor=1,
    skill=HardShot(),
)

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}
