from processor.dataprocessor_service import DataProcessorService

"""
    Main-модуль, т.е. модуль запуска приложений ("точка входа" приложения)
"""

if __name__ == '__main__':
    # Без указания полного пути, программа будет читать файл из своей корневой папки
    DataProcessorService("doctor.csv").run_service()
    DataProcessorService("patient.csv").run_service()
    DataProcessorService("appointment.csv").run_service()
