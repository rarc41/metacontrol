import pathlib
from gui.models.data_storage import DataStorage, read_data

mock = DataStorage()
simulation_data = {'components': ['PROPANE', 'PROPENE'],
                   'therm_method': ['PENG-ROB'],
                   'blocks': ['TOWER'],
                   'streams': ['B', 'D', 'F'],
                   'reactions': [''],
                   'sens_analysis': ['S-1'],
                   'calculators': ['C-1'],
                   'optimizations': ['O-1'],
                   'design_specs': ['']}

input_table_data = [{'Path': r"\Data\Blocks\TOWER\Output\MOLE_RR", 'Alias': 'rr', 'Type': 'Manipulated (MV)'},
                    {'Path': r"\Data\Blocks\TOWER\Output\MOLE_DFR", 'Alias': 'df', 'Type': 'Manipulated (MV)'}]

output_table_data = [{'Path': r"\Data\Streams\D\Output\TOT_FLOW", 'Alias': 'd', 'Type': 'Auxiliary'},
                     {'Path': r"\Data\Streams\B\Output\MOLEFRAC\MIXED\PROPENE", 'Alias': 'xb',
                      'Type': 'Candidate (CV)'},
                     {'Path': r"\Data\Streams\B\Output\TOT_FLOW", 'Alias': 'b', 'Type': 'Auxiliary'},
                     {'Path': r"\Data\Blocks\TOWER\Output\REB_DUTY", 'Alias': 'qr', 'Type': 'Auxiliary'},
                     {'Path': r"\Data\Blocks\TOWER\Output\MOLE_L1", 'Alias': 'l', 'Type': 'Auxiliary'},
                     {'Path': r"\Data\Blocks\TOWER\Output\MOLE_VN", 'Alias': 'v', 'Type': 'Auxiliary'},
                     {'Path': r"\Data\Streams\FEED\Output\TOT_FLOW", 'Alias': 'f', 'Type': 'Auxiliary'},
                     {'Path': r"\Data\Streams\D\Output\MOLEFRAC\MIXED\PROPENE", 'Alias': 'xd',
                      'Type': 'Candidate (CV)'}]

expr_table_data = [{'Name': 'lf', 'Expr': 'l / f', 'Type': 'Candidate (CV)'},
                   {'Name': 'vf', 'Expr': 'v / f', 'Type': 'Candidate (CV)'},
                   {'Name': 'c1', 'Expr': 'qr - 80', 'Type': 'Constraint function'},
                   {'Name': 'c2', 'Expr': '0.995 - xd', 'Type': 'Constraint function'},
                   {'Name': 'j', 'Expr': '-(20*d + (10 - 20*xb)*b - 70*qr)', 'Type': 'Objective function (J)'}]

doe_table_data = {'lb': [7., 0.1],
                  'ub': [25., 0.9],
                  'lhs': {'n_samples': 50, 'n_iter': 100, 'inc_vertices': False},
                  'csv': {'active': True,
                          'filepath': r'C:\Users\Felipe\PycharmProjects\metacontrol\tests\gui\csv_editor\column.csv',
                          'check_flags': [False, False, True, True, True, True, True, True, True, True, True, True],
                          'alias_index': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}}

mock.setSimulationDataDictionary(simulation_data)
mock.setInputTableData(input_table_data)
mock.setOutputTableData(output_table_data)
mock.setExpressionTableData(expr_table_data)
mock.setDoeData(doe_table_data)

sim_file_name = r'C:\Users\Felipe\Desktop\GUI\python\infill.bkp'
out_file = pathlib.Path(__file__).parent / "test_file.mtc"

# write_data(out_file, sim_file_name, mock)
read_data(out_file, DataStorage())