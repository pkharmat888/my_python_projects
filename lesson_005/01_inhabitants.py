# -*- coding: utf-8 -*-

import room_1 as r1, room_2 as r2

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

print('В комнате room_1 живут: ', r1.folks[0] + ' и ' + r1.folks[1])
print('В комнате room_2 живет: ', *r2.folks)
