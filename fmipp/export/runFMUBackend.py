import importlib
import fmipp

def runFMUBackend( backend_class_file_path, backend_class_name ):
    """
    Initialize and run the FMU back-end.

    :param backend_class_file_path: path to file implementing the FMU back-end
    :param backend_class_name: name of class implementing the FMU back-end
    """
    # Creating a ModuleSpec instance based on the path to the class file.
    spec = importlib.util.spec_from_file_location( backend_class_name, backend_class_file_path )

    # Load class inside separate module.
    module = importlib.util.module_from_spec( spec )
    spec.loader.exec_module( module )

    # Retrieve class implementing the FMU back-end.
    backend_class = getattr( module, backend_class_name )

    # Instantiate FMU back-end.
    backend = backend_class()

    try:
        # Initialize the FMU back-end.
        backend._initBackEnd()

        # Enter the simulation loop.
        backend._run()
    except Exception as ex:
        print( ex )