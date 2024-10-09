from pathlib import Path

directory = r'C:\Users\aaraujo\OneDrive - Nelogica\Área de Trabalho\20241008'

counter = 0
files = Path(directory).glob('*')
for file in files:
    if Path(file).suffix == '.ret':
        counter += 1
        file.rename(file.with_suffix('.txt'))
print(f'Arquivos renomeados: {counter}')        
   