from import_tools import data_import

def main():
    import_tool = data_import()
    import_tool.save_nasdaq_stocklist('stockholm')
    import_tool.load_stocklist()
    for el in import_tool.stocklist[:, 1]:
        print('Saving ' + el)
        import_tool.parse_stock_data(el)

    (timestamps, data) = import_tool.load_stock_data(import_tool.stocklist[0, 1])








main()
