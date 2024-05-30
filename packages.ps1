# Activar el entorno virtual de Python
.\venv\Scripts\Activate.ps1

# Actualizar el archivo requirements.txt con las dependencias instaladas
pip freeze > requirements.txt

Write-Host "'requirements.txt' actualizado exitosamente." -ForegroundColor Green

# Obtener la ruta del archivo requirements.txt
$requirementsFilePath = Resolve-Path "requirements.txt"

# Verificar si el archivo requirements.txt existe
if (Test-Path $requirementsFilePath) {
    Write-Host "El archivo 'requirements.txt' se ha encontrado." -ForegroundColor Green

    # Obtener las dependencias actuales instaladas
    $installedPackages = pip freeze

    # Leer el contenido de requirements.txt
    $requiredPackages = Get-Content $requirementsFilePath

    # Comparar las dependencias instaladas con las requeridas
    $packagesToInstall = @()
    foreach ($requiredPackage in $requiredPackages) {
        if ($installedPackages -notcontains $requiredPackage) {
            $packagesToInstall += $requiredPackage
        }
    }

    # Instalar los paquetes que faltan
    if ($packagesToInstall.Count -gt 0) {
        foreach ($package in $packagesToInstall) {
            pip install $package
        }
        Write-Host "Todos los paquetes faltantes han sido instalados exitosamente." -ForegroundColor Green
    } else {
        Write-Host "Todos los paquetes ya están instalados." -ForegroundColor Yellow
    }
} else {
    Write-Host "El archivo 'requirements.txt' no se ha encontrado." -ForegroundColor Red
}
