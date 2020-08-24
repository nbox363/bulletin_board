from .models import SubRubric


def bulletin_board_context_processor(request):
    context = {}
    context['rubrics'] = SubRubric.objects.all()
    return context
