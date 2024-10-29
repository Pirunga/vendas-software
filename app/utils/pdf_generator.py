from fpdf import FPDF
from datetime import date

def generate_pdf_report(data, output_io=None):
    today = date.today().strftime('%Y_%m_%d')
    pdf = FPDF()
    pdf.add_page()

    # Título do Relatório
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Relatório Diário de Vendas', 0, 1, 'C')
    
    # Data do Relatório
    pdf.set_font('Arial', 'I', 12)
    pdf.cell(0, 10, f'Data: {date.today().strftime("%d/%m/%Y")}', 0, 1, 'C')
    pdf.ln(10)  # Espaço entre o título e a tabela

    # Cabeçalho da Tabela
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(100, 10, 'Produto', 1, 0, 'C')
    pdf.cell(50, 10, 'Total de Vendas (R$)', 1, 0, 'C')
    pdf.cell(40, 10, 'Porcentagem (%)', 1, 1, 'C')

    # Total Geral
    total_geral = sum(data.values())

    # Dados da Tabela
    pdf.set_font('Arial', size=10)
    for product, total in data.items():
        porcentagem = (total / total_geral) * 100 if total_geral > 0 else 0 
        pdf.cell(100, 10, product, 1, 0, 'C')
        pdf.cell(50, 10, f'{total:.2f}', 1, 0, 'C')
        pdf.cell(40, 10, f'{porcentagem:.2f}', 1, 1, 'C')

    # Total de Vendas
    pdf.ln(5)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(100, 10, 'Total Geral', 1, 0, 'C')
    pdf.cell(50, 10, f'{total_geral:.2f}', 1, 0, 'C')
    pdf.cell(40, 10, '100.00', 1, 1, 'C')

    # Adicionando rodapé com informações adicionais
    pdf.set_y(-15)
    pdf.set_font('Arial', 'I', 8)
    pdf.cell(0, 10, 'Gerado pelo Sistema de Vendas', 0, 0, 'C')

    # Saída do PDF
    if output_io:
        pdf_bytes = pdf.output(name=f'daily_report_{today}.pdf', dest='S').encode('latin1')
        output_io.write(pdf_bytes)
    else:
        pdf.output(f'daily_report_{today}.pdf')
