import customtkinter
from button_widget.button_widget import ButtonWidget
from entry_widget.entry_widget import EntryWidget
from label_widget.label_widget import LabelWidget
from logo.project_logo import ProjectLogo
from methods.generate_password_method import GeneratePassword
from methods.save_method import SavePassword
from methods.search_password import SearchPassword
from screen_frame.screen_frame import ScreenFrame

# root object for customTkinter
root = customtkinter.CTk()

# screen frame configuration class
screen_frame = ScreenFrame(root=root, title="Password Manager")
screen_frame.show_frame()

# logo configuration class
logo_obj = ProjectLogo(image_path="assets/key.png", tkinter_obj=root)
logo_obj.show_logo()

# label widget objects

# website label
label_obj_website = LabelWidget(root=root, title="Website:", text_color="pink")
label_obj_website.place_label_grid(row=1, column=0)

# email label
label_obj_email = LabelWidget(root=root, title="Email:", text_color="pink")
label_obj_email.place_label_grid(row=2, column=0)

# password label
label_obj_password = LabelWidget(root=root, title="Password:", text_color="pink")
label_obj_password.place_label_grid(row=3, column=0)

# entry widget objects

# website entry
entry_obj_website = EntryWidget(root=root, hint_text="Type website here", width=250)
website_field = entry_obj_website.make_entry()
website_field.grid(row=1, column=1)

# email entry
entry_obj_email = EntryWidget(root=root, hint_text="Type email here", width=250)
email_field = entry_obj_email.make_entry()
email_field.grid(row=2, column=1)
email_field.insert(0, "test@gmail.com")

# password entry
entry_obj_password = EntryWidget(root=root, hint_text="Type password here", width=250)
password_field = entry_obj_password.make_entry()
password_field.grid(row=3, column=1)


# Button widget

# search password callback
search_password = SearchPassword(website_field=website_field)

# search password button
button_obj_search_password = ButtonWidget(root=root, title="Search", on_tap=search_password.search_pass)
search_pass_button = button_obj_search_password.make_button()
search_pass_button.grid(row=1, column=3, padx=(10, 0))

# generate password callback
generate_password = GeneratePassword(password_field=password_field)

# generate password button
button_obj_generate_password = ButtonWidget(root=root, title="Generate", on_tap=generate_password.generate)
gen_pass_button = button_obj_generate_password.make_button()
gen_pass_button.grid(row=3, column=3, padx=(10, 0))

# save password callback
save_password = SavePassword(website_field=website_field, email_field=email_field, password_field=password_field)

# add button
button_obj_add = ButtonWidget(root=root, title="Add", on_tap=save_password.save)
add_button = button_obj_add.make_button()
add_button.grid(row=4, column=1, columnspan=2, pady=10)

root.mainloop()
