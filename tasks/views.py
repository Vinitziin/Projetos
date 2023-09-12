from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import TarefaForm

def adicionar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'tasks/adicionar_tarefa.html', {'form': form})

def listar_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tasks/listar_tarefas.html', {'tarefas': tarefas})

def marcar_como_concluida(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)

    if not tarefa.concluida:
        tarefa.concluida = True
        tarefa.save()

    return redirect('listar_tarefas')

def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)

    if tarefa.concluida:
        tarefa.delete()

    return redirect('listar_tarefas')

def remover_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('listar_tarefas')
    return render(request, 'tasks/remover_tarefa.html', {'tarefa': tarefa})