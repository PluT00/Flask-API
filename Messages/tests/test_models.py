from django.test import TestCase
from Messages.models import Chat, Message
from Users.models import MyUser


class ChatTestCase(TestCase):
    def setUp(self):
        user1 = MyUser.objects.create(username='testuser1', password='testpassword')
        user2 = MyUser.objects.create(username='testuser2', password='testpassword')
        self.chat = Chat()
        self.chat.save()
        self.chat.members.set([user1, user2])

    # Test members many to many field.
    def test_members_related_model(self):
        related_model = self.chat._meta.get_field('members').related_model
        self.assertEqual(related_model, MyUser)

    # Test __str__ function.
    def test_str_function(self):
        str = self.chat.__str__()
        self.assertEqual(str, ", ".join(p.username for p in self.chat.members.all()))


class MessageTestCase(TestCase):
    def setUp(self):
        user = MyUser.objects.create(username='testuser', password='testpassword')
        chat = Chat()
        chat.save()
        chat.members.set([user])
        self.message = Message.objects.create(message='test', chat=chat, author=user)

    # Test message text field.
    def test_message_max_length(self):
        max_length = self.message._meta.get_field('message').max_length
        self.assertEqual(max_length, 10000)

    # Test chat foreign key field.
    def test_chat_realted_model(self):
        related_model = self.message._meta.get_field('chat').related_model
        self.assertEqual(related_model, Chat)

    def test_chat_blank(self):
        blank = self.message._meta.get_field('chat').blank
        self.assertEqual(blank, True)

    def test_chat_null(self):
        null = self.message._meta.get_field('chat').null
        self.assertEqual(null, False)

    # Test author foreign key field.
    def test_aurhor_related_model(self):
        related_model = self.message._meta.get_field('author').related_model
        self.assertEqual(related_model, MyUser)

    def test_author_blank(self):
        blank = self.message._meta.get_field('author').blank
        self.assertEqual(blank, True)

    def test_author_null(self):
        null = self.message._meta.get_field('author').null
        self.assertEqual(null, False)

    # Test datetime date time field.
    def test_datetime_auto_now(self):
        auto_now = self.message._meta.get_field('datetime').auto_now
        self.assertEqual(auto_now, True)

