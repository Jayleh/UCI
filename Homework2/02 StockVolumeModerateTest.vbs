Sub stockTotal():
    
    Dim ws As Worksheet

    For Each ws In Worksheets
        ' Label new column headers
        ws.Range("I1").Value = "Ticker"
        ws.Range("J1").Value = "Yearly Change"
        ws.Range("K1").Value = "Percent Change"
        ws.Range("L1").Value = "Total Stock Volume"
                
        ' Declare ticker letter
        Dim ticker As String
        
        ' Instantiate ticker total
        Dim stock_volume As Double
        stock_volume = 0
        
        ' Declare ticker open and close prices
        Dim open_price, close_price As Double

        ' Declare open and close rows
        Dim open_price_row, close_price_row As Long
        open_price_row = 1
        close_price_row = 1
                
        ' Instantiate ticker count
        Dim ticker_count As Long
        ticker_count = 0
        
        ' Declare yearly and percent changes
        Dim year_change, percent_change As Double
            
        ' Keep track of location of each ticker for summary table
        Dim summary_table_row As Long
        summary_table_row = 2

        ' For the loop
        Dim i, lr As Long
        lr = ws.Cells(Rows.Count, 1).End(xlUp).Row

        ' Loop through all tickers
        For i = 2 To lr

            If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
                ' Set ticker letter
                ticker = ws.Cells(i, 1).Value

                ' Print ticker in summary table
                ws.Range("I" & summary_table_row).Value = ticker

                ' Increase close price row
                close_price_row = close_price_row + 1

                ' Assign open and close prices
                open_price = ws.Cells(open_price_row + ticker_count, 3).Value
                ' close_price = ws.Cells(close_price_row + ticker_count, 6).Value

                ' Calculate yearly difference
                year_change = close_price - open_price

                ' Print yearly change in summary table
                ws.Range("J" & summary_table_row).Value = open_price
                
                ' Calculate percent change
                percent_change = year_change / open_price

                ' Print percent change in summary table
                ws.Range("K" & summary_table_row).Value = percent_change

                ' Increase ticker total
                stock_volume = stock_volume + ws.Cells(i, 7).Value

                ' Print ticker total in summary table
                ws.Range("L" & summary_table_row).Value = stock_volume

                ' Increment summary table row
                summary_table_row = summary_table_row + 1

                ' Reset totals
                ticker_count = 0
                stock_volume = 0
            Else
                ' Default as increase ticker total
                ticker_count = ticker_count + 1
                stock_volume = stock_volume + ws.Cells(i, 7).Value
            End If

        Next i

        ' Autofit columns
        ws.Columns("J").AutoFit
        ws.Columns("K").AutoFit
        ws.Columns("L").AutoFit
        
        ' Format column K to percentage
        ws.Columns("K").EntireColumn.NumberFormat = "0.00%"

        ' Conditionaly format yearly change
        Dim j, summary_table_lr As Long
        summary_table_lr = ws.Cells(Rows.Count, 1).End(xlUp).Row

        For j = 2 To summary_table_lr

            If ws.Range("J" & j).Value > 0 Then
                ws.Range("J" & j).Interior.ColorIndex = 10
            Else
                ws.Range("J" & j).Interior.ColorIndex = 9
            End If

        Next j

    Next ws

End Sub
