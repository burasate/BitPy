import time,os,sys
import importlib
rootPath = os.path.dirname(os.path.abspath(__file__))

os.system('cls||clear')
print('BitPy')
time.sleep(2)
import update

if not os.name == 'nt':
    time.sleep(5)
    update.updateAllFile()

while True:
    try:
        update.updateConfig()
        update.updatePreset()
        update.updateSystem()

        import historical
        importlib.reload(historical)
        historical.updateGSheetHistory()
        historical.loadAllHist(timeFrame='hour')
        #historical.loadAllHist(timeFrame='minute')

        import analysis
        importlib.reload(analysis)
        analysis.getSignalAllPreset()

        import realtime
        update.updateConfig()
        importlib.reload(realtime)
        realtime.AllUser()
        realtime.Reset()

    except Exception as e:
        print('!!!! ==========================')
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print('Error Type {}\nFile {}\n Line {}'.format(exc_type, fname, exc_tb.tb_lineno))
        print('!!!! ==========================')
    finally:
        print('Ending of Process')
        time.sleep(60*2)
        pass