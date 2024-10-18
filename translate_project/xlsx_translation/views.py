from django.shortcuts import render

from django.shortcuts import render, redirect

from django.http import JsonResponse

from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import PasswordResetView

from django.urls import reverse_lazy
from .forms import *
from time import sleep
import os
import glob




@login_required(login_url='/my-login')
def TranslatePage(request):
    

    if request.method=='POST':
        form=UploadForm(request.POST, request.FILES)
        
        
        try:
            request.FILES['file']
            
            
            # print(str(request.FILES['file']).split("."))
            
            if str(request.FILES['file']).split(".")[1].lower()!= 'xlsx':
                messages.error(request, 'Files with only .xlsx extension are allowed!')
                return redirect('translate')
                
            
        
            
        except:
            
            messages.error(request, 'Please upload a file,before submit')
            return redirect('translate')
            
         
      
        
        if form.is_valid() :
            form.save()
            
            #when the form is sucessfully saved, clear the download files
            directory="./converted_data/"
            list_of_files = glob.glob(f'{directory}/*')
                
            for file in list_of_files:
                os.remove(file)
            
            
            messages.success(request, 'File Uploaded Successfully')
            return redirect('translate')
            
            
        else:
            
            context={'form': form}
            return render(request, 'xlsx_translation/translate.html', context)

        
    context={'form': UploadForm() }
                
    return render(request, 'xlsx_translation/translate.html', context)





def get_latest_file_converted():
    directory="./converted_data/"
    
    list_of_files = glob.glob(f'{directory}/*')  # Get all files in the directory
    if not list_of_files:
        return None
    latest_file = max(list_of_files, key=os.path.getmtime)  # Get the latest file based on creation time
    return latest_file

          
    
    
def download_file(request):
    
    file_path=get_latest_file_converted()
    
    if file_path:
                 
        
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename={os.path.basename(file_path)}'
            
                
            
            return response
       
        
    else:
        messages.error(request, "No files Present, Please convert to download the files")
        return redirect('translate')